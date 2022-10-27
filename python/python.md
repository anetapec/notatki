# Orginizing Larger Programs
## Packages
Package in python is a special type of module, it can contain other modules. So you pack modules into packages.
```python
>>> import urllib # this is the package 
>>> import urllib.request # 'request' is a module
<class 'module'>
>>> type(urllib.request)
<class 'module'>
```

### You can check the physical path of the package on the filesystem by `__path__`
```python
>>> import urllib  
>>> urllib.__path__ # only packages have the '__path__'
['/usr/lib/python3.5/urllib']
>>> import urllib.request
>>> urllib.request.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'urllib.request' has no attribute '__path__'
```

`Packages` are represented by directories on the filesystem, when `modules` usually sigle python files.