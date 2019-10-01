from source.evernote_dump.evernote_dump import run_parse

path = '/mnt/data/tmp/evernote'
notes = [
    f'{path}/_archive.enex',
    f'{path}/bike.enex',
    f'{path}/buy.enex',
    f'{path}/car.enex',
    f'{path}/check_lists.enex',
    f'{path}/content.enex',
    f'{path}/it.enex',
    f'{path}/memorable_events.enex',
    f'{path}/persistent_data.enex',
    f'{path}/reference_books.enex',
    f'{path}/tables.enex',
    f'{path}/travels.enex',
    f'{path}/writing.enex',
]
# run_parse(notes, path)

# Plan notes
path = '/mnt/data/tmp/evernote/plans'
notes = [
    f'{path}/2012.enex',
    f'{path}/2013.enex',
    f'{path}/2014.enex',
    f'{path}/2015.enex',
    f'{path}/2016.enex',
]
# run_parse(notes, path)

# Project notes
path = '/mnt/data/tmp/evernote/projects'
notes = [
    f'{path}/DGTI.enex',
    f'{path}/DNNGB.enex',
    f'{path}/my.enex',
    f'{path}/side_job.enex',
    f'{path}/UUGR.enex',
]
run_parse(notes, path)
