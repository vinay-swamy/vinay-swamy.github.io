import bibtexparser 
import argparse

with open('assets/docs/my_papers.bib') as bib:
    bib_db = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bib)

def format_authors(author_string):
    author_list = author_string.split('and')
    out=[]
    for author in author_list:
        author=author.split(',')
        author.reverse()
        out.append(''.join(author))
    return ','.join(out)


for bib in bib_db.entries:
    title=bib['title'].replace(' ','-').replace('{', '').replace('}', '')
    # place holder date since nothing is show
    month_str2int = {'January': 1, "February": 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                     'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    date = f'{bib["year"]}-{month_str2int[bib["month"]]}-01'
    outfile=f'_posts/{date}-{title}.md'
    with open(outfile, 'w+') as md:
        md.write('---\n')# header
        md.write(f'title: {title}\n')
        md.write('layout: post\ncategory: science\n')
        md.write(f'date: {date}\n\nwork-type: Paper\n')
        author_list_formatted = format_authors(bib['author'])
        md.write(f'ref-authors: {author_list_formatted}\n')
        md.write(f'ref-title: {title}\n')
        md.write(f'ref-journal: {bib["journal"]}\n')
        try:
            md.write(f'ref-vol: {bib["volume"]}\n')
        except:
            pass
        md.write(f'ref-doi: {bib["doi"]}\n')
        md.write(f'url: {bib["url"]}\n')
        md.write('---\n')

