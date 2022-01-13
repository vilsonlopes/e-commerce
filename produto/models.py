from PIL import Image
import os
from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do produto')
    descricao_curta = models.TextField(max_length=500)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço Normal')
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name='Preço Promocional')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def __str__(self):
        return self.nome

    def get_preco_formatado(self):
        return f'R$ - {self.preco_marketing:.2f}'.replace('.', ',')
    get_preco_formatado.short_description = 'Preço Normal'

    def get_preco_promo_formatado(self):
        return f'R$ - {self.preco_marketing_promocional:.2f}'.replace('.', ',')
    get_preco_promo_formatado.short_description = 'Preço Promocional'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_heigth = img_pil.size

        if original_width <= new_width:
            print('retornando, largura orignal menor que a nova largura')
            img_pil.close()
            return

        new_heigth = round((new_width * original_heigth) / original_width)
        new_img = img_pil.resize((new_width, new_heigth), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        print('Imagem foi redimensionada.')

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveBigIntegerField(default=1)

    def __str__(self) -> str:
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
