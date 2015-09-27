for key, value in request.data.iteritems():
  if value is None:
    print key
    if getattr(ExistingClassInstance, key) is not None:
      value = getattr(ExistingClassInstance, key)
      print 'VALUE::',value
  setattr(UpdatedObject, key, value)
UpdatedObject.save()
