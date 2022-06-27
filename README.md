# TODO

- fix client_bundle.zip:
  - relative path: server adds 'additional/'. It must be done on client side
  - add only these folders: browser and common
  - manage locking/caching (now it's not thread safe)
  - use a temp folder or in memory
  - compression?
- remove the root package d3. browser/common/server should be in the root
- 