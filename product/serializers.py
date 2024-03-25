from rest_framework import serializers
from product.models import Category, Product, Review, Tag

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'product_count']

    def get_product_count(self, obj):
        return obj.product_set.count()


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'tags']

    def validate_tags(self, value):
        for tag in value:
            if not Tag.objects.filter(pk=tag.pk).exists():
                tag_name = "Tag " + str(tag.pk)
                Tag.objects.create(name=tag_name)
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'product']

class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = 'id reviews average_rating'.split()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']