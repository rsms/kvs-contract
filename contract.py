import storage

# Key-columns table db
tdb = storage.Table(nodes={
  'user_lookup': [ '127.0.0.1:41201', '127.0.0.1:51201' ],
  'user_storage': [ '127.0.0.1:44201', '127.0.0.1:54201' ] })

# Key-value hash db
hdb = storage.KeyValue(protocol='memcached', nodes={
  'avatar_lookup': [ '127.0.0.1:21201', '127.0.0.1:31201' ],
  'avatar_storage': [ '127.0.0.1:24201', '127.0.0.1:34201' ] })

# Key-value b tree db
bdb = storage.KeyValue(filename='/tmp/test.bdb')
# Type (b tree) is deduced from filename extension and can be explicitly set
# using an argument like this: type='b' 

# ---------------------------------------------------------------------------
# Operations on any/all types:

# mapping:
hdb['johndoe'] # raise KeyError
del hdb['johndoe'] # raise KeyError
'johndoe' in avatars # => False
hdb['johndoe'] = 'hello'
hdb['johndoe'] # => 'hello'
len(hdb) # => 1
del hdb['johndoe']
len(hdb) # => 0

# methods:
hdb.get('kate') # => None
hdb.get('kate', 'hej') # => 'hej'
hdb.get('kate') # => None
hdb.set('kate', 'interwebs')
hdb.get('kate') # => 'interwebs'
hdb.keys() # => ('kate', )
hdb.values() # => ('interwebs', )
hdb.items() # => (('kate', 'interwebs), )
hdb.clear()
len(hdb) # => 0
hdb.copy() # raise NotImplementedError
hdb.popitem() # raise NotImplementedError
hdb.update({'cat':'small', 'dog':'large'})
len(hdb) # => 2
hdb.remove('kate') # => None

# ---------------------------------------------------------------------------
# Operations on b tree and hash db
hdb.incr('visitors')
hdb.incr('visitors')
hdb['visitors'] # => 2
hdb.decr('visitors')
hdb['visitors'] # => 1

# ---------------------------------------------------------------------------
# Operations on b tree db
bdb['mary'] = 'Mary Parkins'
bdb['kent'] = 'Kent Bulgur'
bdb['mos'] = 'Mos Default'
cur = bdb.get_cursor('kent') # => BDBCursor
cur.next() # => ('kent', 'Kent Bulgur')
cur.next() # => ('mary', 'Mary Parkins')
cur.next() # => ('mos', 'Mos Default')
cur.next() # raise StopIteration
cur = bdb.get_cursor('mary') # => BDBCursor
cur.next() # => ('mary', 'Mary Parkins')
cur.next() # => ('mos', 'Mos Default')
cur.next() # raise StopIteration
for row in bdb.get_cursor('mary'):
  print row

# ---------------------------------------------------------------------------
# Operations on table db
tdb.get_cell('john', 'age') # => '32'
tdb.set_cell('john', 'age', '4')
tdb.remove_cell('john', 'age')
tdb.get_cell('john', 'age') # => None
tdb.has_cell('john', 'age') # => False
