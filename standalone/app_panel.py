import panel as pn


def show_date_picker():
    pn.extension()

    start_date = pn.widgets.DatePicker(name='Start Date')
    end_date = pn.widgets.DatePicker(name='End Date')

    wb = pn.WidgetBox('## Query Parameters', start_date, end_date)

    pn.Row(wb, ).servable(target='date-widgets')


show_date_picker()
