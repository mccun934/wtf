import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://username:password@localhost/project_db')
db_session = scoped_session(sessionmaker(bind=engine))

class Organization(SQLAlchemyObjectType):  
    class Meta:
        model = OrganizationModel
        interfaces = (graphene.relay.Node, )

class Label(SQLAlchemyObjectType):
    class Meta:
        model = LabelModel
        interfaces = (graphene.relay.Node, )

class User(SQLAlchemyObjectType):
   class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node, )

class Project(SQLAlchemyObjectType):
    class Meta:
        model = ProjectModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    organizations = SQLAlchemyConnectionField(Organization)
    users = SQLAlchemyConnectionField(User)
    projects = SQLAlchemyConnectionField(Project)

schema = graphene.Schema(query=Query)

# Create Flask app
app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
