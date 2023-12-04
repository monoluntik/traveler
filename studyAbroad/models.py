from django.db import models
from django_countries.fields import CountryField
# Create your models here.
from django_quill.fields import QuillField
CH_type_of_training = (
        # ('Все', 'Все'),
        ('Языковые курсы', 'Языковые курсы'),
        ('Бакалавриат', 'Бакалавриат'),
        ('Магистратура', 'Магистратура'),
        ('Средняя школа', 'Средняя школа'),
        ('Каникулы', 'Каникулы'),
        ('Дипломная программа', 'Дипломная программа'),
        ('Постдипломная программа', 'Постдипломная программа'),
        ('Сертификат', 'Сертификат'),
    )

CH_language = (
        # ('', 'Любой язык'),
        ('Английский', 'Английский'),
        ('Немецкий', 'Немецкий'),
        ('Французский', 'Французский'),
        ('Китайский', 'Китайский'),
        ('Польский', 'Польский'),
        ('Чешский', 'Чешский'),
        ('Испанский', 'Испанский'),
        ('Русский', 'Русский'),
        ('Латышский', 'Латышский'),
    )

CH_accommodation = (
        ('В семье', 'В семье'),
        ('В общежитии', 'В общежитии'),
        ('В отеле', 'В отеле'),
        ('В пансионе', 'В пансионе'),
        ('В резиденции', 'В резиденции'),
    )
CH_for_whome = (
        ('Студентам','Студентам'),
        ('Взрослым','Взрослым'),
        ('Школьникам','Школьникам'),
        ('Детям','Детям')
    )
class StudyAbroad(models.Model):
    name = models.CharField(max_length=555)
    country = CountryField()
    type_of_training = models.CharField(choices=CH_type_of_training, max_length=255)
    language = models.CharField(choices=CH_language, max_length=255)
    accommodation = models.CharField(choices=CH_accommodation,  max_length=255 )
    price_kgs = models.FloatField(default=0)
    price_usd = models.FloatField(default=0)

    features_of_the_program = models.CharField(max_length=255,verbose_name='Особенности программы')
    direction = models.TextField(verbose_name='Направление')
    deadline_for_submission_of_documents = models.CharField(max_length=255,verbose_name='Дедлайн приема документов')
    duration_of_the_program = models.CharField(max_length=255,verbose_name='Длительность программы')
    description = QuillField()
    document = models.FileField(upload_to='media/documents/')
    

class StudyAbroadForWhome(models.Model):
    for_whome = models.CharField(choices=CH_for_whome, max_length=255)
    study_abroad = models.ForeignKey(StudyAbroad, on_delete=models.CASCADE, related_name='for_whomes')    

class StudyAbriadAdditional(models.Model):
    name = models.CharField(choices=(
        ('Программа', 'Программа'),
        ('Галерея', 'Галерея'),
        ('Требования', 'Требования'),
        ('Проживание', 'Проживание'),
        ('Цены и сроки', 'Цены и сроки'),
    ),max_length=355)
    description = QuillField()
    study_abroad = models.ForeignKey(StudyAbroad, on_delete=models.CASCADE, related_name='additional')


class StudyAbroadImage(models.Model):
    study_abroad = models.ForeignKey(StudyAbroad, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()