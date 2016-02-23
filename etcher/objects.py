class SpatialObject():
    center_x = 0
    center_y = 0
    height = 0
    width = 0

    def __init__(self, x, y, h, w):
        self.center_x = x
        self.center_y = y
        self.height = h
        self.width = w


class KeyCap(SpatialObject):
    jig_label = ''
    shape = ()

    def __init__(self, x, y, h, w, label):
        self.jig_label = label
        self.shape = (1, 1)  # default 1x1
        super(KeyCap, self).__init__(x, y, h, w)

    def __repr__(self):
        return('<{} "{}" ({}x{})>'.format(
            self.__class__.__name__,
            self.jig_label,
            self.shape[0],
            self.shape[1]
        ))
