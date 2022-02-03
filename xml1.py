import xml.etree.ElementTree as ET

data = '''
<stuff>
<persons>
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>
    <person>
        <name>Mason</name>
        <phone type="local">
            734 303 4456
        </phone>
        <email hide="no"/>
    </person>
</persons>
</stuff>
'''

tree = ET.fromstring(data)
allpersons = tree.findall('persons/person')
print('count:', len(allpersons))
for person in allpersons:
    print('Name:', person.find('name').text)
    print('Attr:', person.find('email').get('hide'))
