from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Organization(Base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Label(Base):
    __tablename__ = 'label'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    organization = relationship("Organization")

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey('organization.id'))
    parent_project_id = Column(Integer, ForeignKey('project.id'))
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    organization = relationship("Organization")
    parent_project = relationship("Project", remote_side=[id])

# Many-to-many association tables
customer_project = Table('customer_project', Base.metadata,
    Column('customer_id', Integer, ForeignKey('customer.id')),
    Column('project_id', Integer, ForeignKey('project.id'))
)

customer_label = Table('customer_label', Base.metadata,
    Column('customer_id', Integer, ForeignKey('customer.id')),
    Column('label_id', Integer, ForeignKey('label.id'))
)

project_label = Table('project_label', Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('label_id', Integer, ForeignKey('label.id'))
)

# Add relationships to Customer and Project classes
Customer.projects = relationship("Project", secondary=customer_project, backref="customers")
Customer.labels = relationship("Label", secondary=customer_label, backref="customers")

Project.labels = relationship("Label", secondary=project_label, backref="projects")

class CustomerData(Base):
    __tablename__ = 'customer_data'
    customer_id = Column(Integer, ForeignKey('customer.id'), primary_key=True)
    key = Column(String, primary_key=True)
    value = Column(String)
    customer = relationship("Customer")

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

class OrganizationObject(SQLAlchemyObjectType):
    class Meta:
        model = Organization

class LabelObject(SQLAlchemyObjectType):
    class Meta:
        model = Label

class CustomerObject(SQLAlchemyObjectType):
    class Meta:
        model = Customer

class ProjectObject(SQLAlchemyObjectType):
    class Meta:
        model = Project

class CustomerDataObject(SQLAlchemyObjectType):
    class Meta:
        model = CustomerData


class Query(graphene.ObjectType):
    all_organizations = graphene.List(OrganizationObject)
    all_labels = graphene.List(LabelObject)
    all_customers = graphene.List(CustomerObject)
    all_projects = graphene.List(ProjectObject)
    all_customer_data = graphene.List(CustomerDataObject)

    def resolve_all_organizations(self, info):
        query = OrganizationObject.get_query(info)
        return query.all()

    def resolve_all_labels(self, info):
        query = LabelObject.get_query(info)
        return query.all()

    def resolve_all_customers(self, info):
        query = CustomerObject.get_query(info)
        return query.all()

    def resolve_all_projects(self, info):
        query = ProjectObject.get_query(info)
        return query.all()

    def resolve_all_customer_data(self, info):
        query = CustomerDataObject.get_query(info)
        return query.all()
