import xadmin
from .models import *

xadmin.site.register(Ads)
xadmin.site.register(Category)

class ArticleAdmin:
    style_fields = {"body": "ueditor"}

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Tag)