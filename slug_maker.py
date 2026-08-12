def slug_maker(title):
    slug = title.strip().lower()
    slug = slug.replace(',', '').replace('.', '')
    slug = slug.replace(' ', '-')
    return slug

# Implement slug_maker(title).
# Remove leading and trailing spaces, convert the text to lowercase, remove commas and periods, and replace spaces with hyphens.
# Return the final slug.