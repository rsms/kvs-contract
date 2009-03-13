import storage

users = storage.TyrantTable(nodes={
  'user_lookup': [ '127.0.0.1:41201', '127.0.0.1:51201' ],
  'user_storage': [ '127.0.0.1:44201', '127.0.0.1:54201' ] })

avatars = storage.MemcachedKeyValue(nodes={
  'avatar_lookup': [ '127.0.0.1:21201', '127.0.0.1:31201' ],
  'avatar_storage': [ '127.0.0.1:24201', '127.0.0.1:34201' ] })

user = users.get('johndoe')
print user['age'] # => '32'
users.set('johndoe', {'name':'John Doe', 'age':41})
user = users.get('johndoe')
print user['age'] # => '41'

avatar = avatars.get('johndoe')
print avatar # => 'GIF89a...blinksdf\0xsdf.sd f'
avatar = avatars.delete('johndoe')
avatar = avatars.get('johndoe') # => None

print avatars['johndoe'] # raise KeyError
del avatars['johndoe'] # raise KeyError
avatars['johndoe'] = 'hello'
avatars['johndoe'] # => 'hello'
