import graphene
from graphene_django.types import DjangoObjectType
from .models import Pogoda, Review, Participant, UserProfile, Pogoda
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class PogodaType(DjangoObjectType):
    class Meta:
        model = Pogoda


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class ParticipantType(DjangoObjectType):
    class Meta:
        model = Participant


class Query(graphene.ObjectType):
    all_pogoda = graphene.List(PogodaType)
    pogoda = graphene.Field(PogodaType, id=graphene.ID(required=True))
    all_users = graphene.List(UserType)
    all_profiles = graphene.List(UserProfileType)

    def resolve_all_pogoda(self, info, **kwargs):
        return Pogoda.objects.all()

    def resolve_pogoda(self, info, id):
        return Pogoda.objects.get(pk=id)

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_profiles(self, info):
        return UserProfile.objects.all()


class CreateReview(graphene.Mutation):
    class Arguments:
        pogoda_id = graphene.ID(required=True)
        rating = graphene.Int(required=True)
        comment = graphene.String()

    review = graphene.Field(ReviewType)

    def mutate(self, info, pogoda_id, rating, comment=""):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Musisz być zalogowany")

        pogoda = Pogoda.objects.get(pk=pogoda_id)

        if Review.objects.filter(user=user, pogoda=pogoda).exists():
            raise Exception("Już oceniłeś to wydarzenie")

        review = Review.objects.create(user=user, pogoda=pogoda, rating=rating, comment=comment)
        return CreateReview(review=review)


class Mutation(graphene.ObjectType):
    create_review = CreateReview.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)