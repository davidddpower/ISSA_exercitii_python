def build_xml_element(tag, content, **attributes):
    # Creeaza lista cu atributele elementului XML
    attr_parts = []

    # Adauga fiecare atribut in formatul XML corespunzator
    for key, value in attributes.items():
        attr_name = key.replace('_', '-') if key.startswith('_') else key
        attr_parts.append(f'{attr_name}="{value}"')

    # Construieste stringul XML
    attrs = ' '.join(attr_parts)
    if attrs:
        return f'<{tag} {attrs}>{content}</{tag}>'
    return f'<{tag}>{content}</{tag}>'


# Exemplu de utilizare
print(build_xml_element('a', 'Hello there', href='http://python.org', _class='my-link', id='someid'))
