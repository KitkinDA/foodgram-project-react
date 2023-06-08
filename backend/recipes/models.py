from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Tag(models.Model):
    """Модель тегов"""

    name = models.CharField(verbose_name="Название", max_length=200)
    color = models.CharField(
        max_length=7,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name="Уникальный слаг",
        max_length=200,
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингредиентов"""

    name = models.CharField(verbose_name="Название", max_length=200)
    measurement_unit = models.CharField(
        verbose_name="Единицы измерения", max_length=200
    )

    class Meta:
        ordering = ("-name",)
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Модель для связи рецептов и ингредиентов."""

    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="ingredient_list",
        verbose_name="Рецепт",
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe",
        verbose_name="Ингредиент",
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Количество",
        validators=[
            MinValueValidator(1, message="Минимальное количество: 1"),
        ],
    )

    class Meta:
        verbose_name = "Ингредиент рецепта"
        verbose_name_plural = "Ингредиенты рецепта"
        ordering = ("-id",)
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "ingredient"], name="unique ingredient"
            )
        ]


class Recipe(models.Model):
    """Модель рецептов"""

    author = models.ForeignKey(
        User, verbose_name="Автор",
        related_name="recipes",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(
        upload_to="recipes/", verbose_name="Изображение",
        blank=True,
    )
    text = models.TextField(verbose_name="Описание")
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="recipes",
        verbose_name="Ингредиенты",
        through=RecipeIngredient,
    )
    tags = models.ManyToManyField(
        Tag, related_name="recipes", verbose_name="Теги")
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name="Время приготовления (в минутах)",
        validators=[
            MinValueValidator(1, message="Минимальное время: 1"),
        ],
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name[:10]


class Follow(models.Model):
    """Модель подписок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author",
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_author_unique",
        verbose_name="Автор",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "author"], name="unique_follow"),
        ]


class Favourite(models.Model):
    """Модель избранных рецептов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Рецепт",
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"], name="user_recipe_unique"
            ),
        ]


class Cart(models.Model):
    """Модель списка покупок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shopping_cart",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="shopping_cart",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"], name="unique_purchase"),
        ]
