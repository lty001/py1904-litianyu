import xadmin
from .models import *

class CommentAdminx(object):
    list_display=['name','content','create_time','goods']

xadmin.site.register(Comment,CommentAdminx)