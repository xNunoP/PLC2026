import re


def processar_cabecalho(match):
    nivel = len(match.group(1)) 
    texto = match.group(2)
    return f"<h{nivel}>{texto}</h{nivel}>"

def markdown_para_html(texto_md):
    html = texto_md
    
    # 1. Cabeçalhos (Headers)
    html = re.sub(r'(?m)^(#+)\s+(.*)', processar_cabecalho, html)
    
    # 2. Bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)
    
    # 3. Itálico
    html = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html)
    
    # 4. Imagens
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', html)
    
    # 5. Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    
    # 6. Listas Numeradas
    html = re.sub(r'(?m)^\d+\.\s+(.*)', r'<li>\1</li>', html)
    html = re.sub(r'((?:<li>.*?</li>\n?)+)', r'<ol>\n\1</ol>', html)
    
    return html
