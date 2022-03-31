from ckeditor.fields import RichTextField
from django.db import models
from django_resized import ResizedImageField


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

    def get_category_products(self):
        return Product.objects.filter(category___pk=self.pk)


class ProductTag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Product Tags'
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_tag_products(self):
        return Product.objects.filter(tags__pk=self.pk)


class ProductBrand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_brand_products(self):
        return Product.objects.filter(brand___pk=self.pk)


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Unique name for product")
    description = models.TextField(
        default="Please provide description for this product, description is required for better understanding",
        help_text="Please provide description for this product, description is required for better understanding"
    )
    detailed_description = RichTextField()
    image = ResizedImageField(
        upload_to='product/image/', null=False, blank=False, help_text="Image must be of png and size of [500*500]",
        size=[300, 300], crop=['middle', 'center'], quality=75, force_format='PNG'
    )
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, help_text="Select product category")
    brand = models.ForeignKey(
        ProductBrand, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Select product brand, if no brands for this just leave it blank"
    )
    tags = models.ManyToManyField(ProductTag)
    retail_price = models.FloatField(default=1)
    sale_price = models.FloatField(default=1)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_product_images(self):
        return ProductImage.objects.filter(product__pk=self.pk)


class ProductImage(models.Model):
    image = ResizedImageField(
        upload_to='product/images/', null=False, blank=False, help_text="Image must be of png and size of [500*500]",
        size=[300, 300], crop=['middle', 'center'], quality=75, force_format='PNG'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['product', '-id']
        verbose_name_plural = "Product Images"

