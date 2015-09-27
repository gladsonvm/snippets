for key, value in request.data.iteritems():
  if value is None:
    print key
    if getattr(ExistingBooking, key) is not None:
      value = getattr(ExistingBooking, key)
      print 'VALUE::',value
  setattr(Bookingupdate, key, value)
Bookingupdate.save()
