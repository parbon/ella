# register admin options
import ella.media.admin

# queue register
from ella.media.models import Media, FormattedFile
from ella.media.queue import QUEUE as ELLA_QUEUE
ELLA_QUEUE.register('ella/media/formattedfile', FormattedFile.objects.create_from_queue)
ELLA_QUEUE.register('ella/media/source', Media.objects.create_from_queue)

