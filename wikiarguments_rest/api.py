from flask import abort
from flask.ext.restful import Api, Resource, reqparse, marshal, types
from flask.ext.restful.fields import String, Raw

from wikiarguments_rest import app
from wikiarguments_rest.datamodel import Question


api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return dict(hello="world")


class QuestionResource(Resource):
    fields = dict(
        url=String,
        questionId=Raw,
        score=Raw,
        dateAdded=Raw,
        title=String
    )
    fields_with_detail = dict(
            details=String
    )
    fields_with_detail.update(fields)
    parser = reqparse.RequestParser()
    parser.add_argument("details", type=types.natural, default=0)

    def get(self, question_url):
        args = QuestionResource.parser.parse_args()
        question = Question.query.filter_by(url=question_url).one()
        print(args)
        if args["details"]:
            return marshal(question, QuestionResource.fields_with_detail)
        else:
            return marshal(question, QuestionResource.fields)


class QuestionURLFormatter(Raw):
    def format(self, question: Question):
        return question.url


class ArgumentResource(Resource):
    fields = dict(
        url=String,
        argumentId=Raw,
        abstract=String,
        score=Raw,
        dateAdded=Raw,
        type=Raw,
        question_url=QuestionURLFormatter(attribute="question"),
        headline=String)
    fields_with_detail = dict(
            details=String)
    fields_with_detail.update(fields)
    parser = reqparse.RequestParser()
    parser.add_argument("details", type=types.natural, default=0)

    def get(self, question_url: str, argument_url: str):
        question = Question.query.filter_by(url=question_url).first_or_404()
        args = ArgumentResource.parser.parse_args()
        argument = list(filter(lambda a: a.url == argument_url, question.arguments))
        if not argument:
            abort(404)
        fields = ArgumentResource.fields_with_detail if args["details"] else ArgumentResource.fields
        return marshal(argument[0], fields)


class ArgumentsResource(ArgumentResource):
    def get(self, question_url: str):
        question = Question.query.filter_by(url=question_url).first_or_404()
        args = ArgumentsResource.parser.parse_args()
        print(args)
        direct_arguments = list(filter(lambda a: a.parentId == 0, question.arguments))
        fields = ArgumentResource.fields_with_detail if args["details"] else ArgumentResource.fields
        return marshal(direct_arguments, fields)
        

api.add_resource(HelloWorld, "/hello")
api.add_resource(QuestionResource, "/questions/<string:question_url>")
api.add_resource(ArgumentResource, "/questions/<string:question_url>/arguments/<string:argument_url>")
api.add_resource(ArgumentsResource, "/questions/<string:question_url>/arguments")
