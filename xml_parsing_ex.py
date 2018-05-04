import xml.dom.minidom


def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("my_xml.xml")

    # print out the document node and the name of the first child tag
    print doc.nodeName
    print doc.firstChild.tagName

    # get a list of XML tags from the document and print each one
    expertise = doc.getElementsByTagName("expertise")
    print "%d expertise:" % expertise.length
    for skill in expertise:
        print skill.getAttribute("abc")

    # create a new XML tag and add it into the document
    newexpertise = doc.createElement("expertise")
    newexpertise.setAttribute("abc", "BigData")
    doc.firstChild.appendChild(newexpertise)
    print " "

    expertise = doc.getElementsByTagName("expertise")
    print "%d expertise:" % expertise.length
    for skill in expertise:
        print skill.getAttribute("abc")

if __name__ == "__main__":
  main()
