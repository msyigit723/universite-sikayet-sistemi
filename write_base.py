import os

content = """{%% load static %%}
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{%% block title %%}\u00dcniversite \u015eikayet Sistemi{%% endblock %%}</title>
    <meta name="description" content="\u00dcniversite \u00f6\u011frencileri i\u00e7in modern \u015fikayet ve talep y\u00f6netim sistemi">
    <link rel="stylesheet" href="{%% static 'tickets/style.css' %%}">
</head>
<body>
    <nav class="navbar">
        <div class="navbar-inner">
            <a href="{%% url 'anasayfa' %%}" class="navbar-brand">
                <span class="logo-icon">\U0001f393</span>
                <span>\u015eikayet Sistemi</span>
            </a>
            <ul class="navbar-links">
                <li><a href="{%% url 'anasayfa' %%}">\U0001f3e0 Anasayfa</a></li>
                {%% if user.is_authenticated %%}
                    <li><a href="{%% url 'panel' %%}">\U0001f4ca Panelim</a></li>
                    {%% if user.is_staff %%}
                        <li><a href="{%% url 'yonetim_paneli' %%}">\u2699\ufe0f Y\u00f6netim</a></li>
                    {%% endif %%}
                    <li><a href="{%% url 'talep_olustur' %%}" class="btn-nav">\u270f\ufe0f Yeni \u015eikayet</a></li>
                    <li><a href="{%% url 'cikis' %%}" class="btn-nav-outline">\U0001f6aa \u00c7\u0131k\u0131\u015f</a></li>
                {%% else %%}
                    <li><a href="{%% url 'giris' %%}">\U0001f511 Giri\u015f</a></li>
                    <li><a href="{%% url 'kayit' %%}" class="btn-nav">\U0001f4dd Kay\u0131t Ol</a></li>
                {%% endif %%}
            </ul>
        </div>
    </nav>
    <div class="container">
        {%% if messages %%}
            <ul class="messages">
                {%% for message in messages %%}
                    <li class="message message-{{ message.tags }}">
                        {%% if message.tags == 'success' %%}\u2705{%% elif message.tags == 'error' %%}\u274c{%% elif message.tags == 'info' %%}\u2139\ufe0f{%% else %%}\u26a0\ufe0f{%% endif %%}
                        {{ message }}
                    </li>
                {%% endfor %%}
            </ul>
        {%% endif %%}
        {%% block content %%}{%% endblock %%}
    </div>
    <footer class="footer">
        <p>\u00a9 2026 \u00dcniversite \u015eikayet Sistemi \u2014 T\u00fcm haklar\u0131 sakl\u0131d\u0131r.</p>
    </footer>
</body>
</html>"""

# Replace doubled percent signs with single
content = content.replace('%%', '%')

path = os.path.join('tickets', 'templates', 'tickets', 'base.html')
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('base.html written successfully!')
print('First 500 chars:')
with open(path, 'r', encoding='utf-8') as f:
    print(repr(f.read()[:500]))
