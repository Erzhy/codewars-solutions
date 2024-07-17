def domain_name(url):
    
    if url.startswith('http') or url.startswith('www'):
        url_splited_by_dot = url.split('.')
    
        first_part = url_splited_by_dot[0]
    
        if first_part.startswith('www'):
            return url_splited_by_dot[1]
        if first_part.startswith('http') and first_part.endswith('www'):
            return url_splited_by_dot[1]
        return first_part.split('//')[1]
    return url.split('.')[0]
