from guest import Guest
from event import Event
from template import Template
from eventguest import EventGuest
from database import create_database, engine, session

if __name__ == '__main__':
    pass
    """create_database(engine)
    e = Event()
    e.invitor_name = 'Mikki'
    e.party_place = 'some place goed'
    e.party_date = '2022-09-12'
    e.party_start = '17:08:00'
    e.party_end = '20:08:00'
    session.add(e)
    session.commit()

    t = Template()
    t.name = 'Birthday'
    t.content = 'Dear {{guest.name}}, My birthday is coming soon. Could you join me at {{event.party_place}}'
    session.add(t)
    session.commit()

    g = Guest()
    g.first_name = 'Leon'
    g.last_name = 'Van Koek'
    session.add(g)
    session.commit()

    eg = EventGuest()
    eg.id_event = 1
    eg.id_guest = 1
    session.add(eg)
    session.commit()
    e = session.query(Event).get(1)
    e.template_id = 1
    session.add(e)
    session.commit()
"""
