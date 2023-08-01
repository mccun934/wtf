from flask import Flask
from flask_graphql import GraphQLView
import graphene
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api import Query

app = Flask(__name__)

# Setup the SQLAlchemy database engine
engine = create_engine('postgresql://username:password@localhost/wtf', echo=True)
Session = sessionmaker(bind=engine)

# Required for SQLAlchemy session management
@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.close_all()

schema = graphene.Schema(query=Query)  # Add "mutation=Mutation" if you have defined mutations

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,  # for having the GraphiQL interface
        context={'session': Session}
    )
)

if __name__ == '__main__':
    app.run()
