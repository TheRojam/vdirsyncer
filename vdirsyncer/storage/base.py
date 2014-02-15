class Item(object):
    '''wrapper class for VCALENDAR and VCARD'''
    def __init__(self, raw):
        self.raw = raw
        self._uid = None

    @property
    def uid(self):
        for line in raw.splitlines():
            if line.startswith(b'UID'):
                return line.lstrip(b'UID:').strip()


class Storage(object):
    def __init__(self, fileext, item_class=Item):
        self.fileext = fileext
        self.item_class = item_class

    def list_items(self):
        '''
        :returns: list of (href, etag)
        '''
        raise NotImplementedError()

    def get_items(self, hrefs):
        '''
        :param hrefs: list of hrefs to fetch
        :returns: list of (object, href, etag)
        '''
        raise NotImplementedError()

    def item_exists(self, href):
        '''
        check if item exists
        :returns: True or False
        '''
        raise NotImplementedError()

    def upload(self, obj):
        '''
        Upload a new object, raise
        :exc:`vdirsyncer.exceptions.AlreadyExistingError` if it already exists.
        :returns: (href, etag)
        '''
        raise NotImplementedError()

    def update(self, obj, etag):
        '''
        Update the object, raise :exc:`vdirsyncer.exceptions.WrongEtagError` if
        the etag on the server doesn't match the given etag, raise
        :exc:`vdirsyncer.exceptions.NotFoundError` if the item doesn't exist.

        :returns: etag on the server
        '''
        raise NotImplementedError()