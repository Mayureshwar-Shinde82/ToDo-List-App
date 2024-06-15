from graphene import ObjectType, String, Field, Int, List, Schema, Mutation
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import ToDo as ToDoModel
from . import db

class ToDo(SQLAlchemyObjectType):
    class Meta:
        model = ToDoModel

class Query(ObjectType):
    all_todos = SQLAlchemyConnectionField(ToDo.connection)
    todo = Field(ToDo, id=Int(required=True))

    def resolve_todo(self, info, id):
        query = ToDo.get_query(info)
        return query.get(id)

class CreateToDo(Mutation):
    class Arguments:
        title = String(required=True)
        description = String(required=True)
        time = String(required=True)
        image = String()

    todo = Field(lambda: ToDo)

    def mutate(self, info, title, description, time, image=None):
        user_id = info.context['user_id']
        todo = ToDoModel(title=title, description=description, time=time, image=image, user_id=user_id)
        db.session.add(todo)
        db.session.commit()
        return CreateToDo(todo=todo)

class DeleteToDo(Mutation):
    class Arguments:
        id = Int(required=True)

    success = Field(lambda: Boolean)

    def mutate(self, info, id):
        user_id = info.context['user_id']
        todo = ToDoModel.query.get(id)
        if todo and todo.user_id == user_id:
            db.session.delete(todo)
            db.session.commit()
            return DeleteToDo(success=True)
        return DeleteToDo(success=False)

class UpdateToDo(Mutation):
    class Arguments:
        id = Int(required=True)
        title = String()
        description = String()
        time = String()
        image = String()

    todo = Field(lambda: ToDo)

    def mutate(self, info, id, title=None, description=None, time=None, image=None):
        user_id = info.context['user_id']
        todo = ToDoModel.query.get(id)
        if todo and todo.user_id == user_id:
            if title:
                todo.title = title
            if description:
                todo.description = description
            if time:
                todo.time = time
            if image:
                todo.image = image
            db.session.commit()
            return UpdateToDo(todo=todo)
        return UpdateToDo(todo=None)

class Mutation(ObjectType):
    create_todo = CreateToDo.Field()
    delete_todo = DeleteToDo.Field()
    update_todo = UpdateToDo.Field()

schema = Schema(query=Query, mutation=Mutation)
