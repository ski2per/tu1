import urwid
from tui import conf


class AppHeader(urwid.WidgetWrap):
    header_text = ('header',  conf.HEADER_TEXT)

    def __init__(self):
        self.debug = urwid.AttrWrap(urwid.Text('DEBUG'), 'debug')
        self.debug2 = urwid.AttrWrap(urwid.Text('DEBUG2'), 'debug')

        widget_list = [
            urwid.AttrWrap(urwid.Text(self.header_text), 'header'),
            self.debug,
            self.debug2,
        ]
        super().__init__(urwid.Columns(widget_list))


class AppFooter(urwid.WidgetWrap):
    footer_text = ('footer', conf.FOOTER_TEXT)

    def __init__(self):
        widget = urwid.AttrWrap(urwid.Text(self.footer_text), 'footer')
        super().__init__(widget)


class PopupDialog(urwid.WidgetPlaceholder):
    signals = ['quit_event']

    def __init__(self):
        super().__init__(urwid.SolidFill(' '))
        content = [
            urwid.Text(("warning", "Quit Setup Wizard ?")),
            urwid.Divider(),
            urwid.Columns([
                urwid.Padding(urwid.AttrWrap(urwid.Button('Yes', on_press=self._emit_quit_event), 'button'),
                              min_width=conf.POPUP_BTN_WIDTH, right=1),
                urwid.Padding(urwid.AttrWrap(urwid.Button('No', on_press=self._emit_quit_event), 'button'),
                              min_width=conf.POPUP_BTN_WIDTH, left=1),
            ])
        ]
        tmp = urwid.ListBox(urwid.SimpleListWalker(content))
        # origin = urwid.Pile(content)
        self.origin = urwid.Padding(tmp, align='center', width=('relative', conf.DEFAULT_WIDTH_PERCENTAGE))

    def open(self):
        self.original_widget = urwid.Overlay(urwid.LineBox(self.origin), self.original_widget,
                                             align='center', width=conf.POPUP_WIDTH,
                                             valign='middle', height=conf.POPUP_HEIGHT)

    def _emit_quit_event(self, *args):
        self._emit('quit_event', args)


class JobBar(urwid.WidgetWrap):
    def __init__(self, text, status):
        self._text = text
        self._status = status
        # widget = urwid.Text(self._format_text())
        self._title_component = urwid.Text(self._text)
        # self._status_component = urwid.AttrWrap(urwid.Text(self._status), 'background')
        self._status_component = urwid.Text(self._status)

        bar = urwid.Columns([
            urwid.Padding(self._title_component, width=('relative', 80), align='right'),
            urwid.Padding(self._status_component, width=16, align='left')
        ])
        widget = urwid.Pile([
            bar,
            urwid.Divider()
        ])

        super().__init__(widget)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
        self._status_component.set_text(status)

