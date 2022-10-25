def build_xml_element(tag, content, **props):
    str = "<{} ".format(tag)
    for key, value in props.items():
        str += '{}="{}"'.format(key, value)
    str += ">{}</{}>".format(content, tag)
    return str


print(build_xml_element("a", "Hello there",
      href=" http://python.org ", _class=" my-link ", id=" someid "))
