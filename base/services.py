from django.core.exceptions import ValidationError


def get_path_avatar(instance, file):
    """ Построение пути к файлу, формат: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instance.id}/{file}'


def get_path_file(instance, file):
    """ Построение пути к файлу, формат: (media)/file/user_id/file
    """
    return f'file/{instance.id}/{file}'

def validate_size_image(file_obj):
    max_size = 2

    if file_obj.size > max_size * 1024 * 1024:
        raise ValidationError(f'Максимальный размер файла превышает {max_size}MB')
