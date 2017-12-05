class AbstractPage(object):
    _page_driver_ = None

    def __init__(self, driver):
        self._driver = driver