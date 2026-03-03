"""
Bu script tüm template dosyalarını düzgün şekilde yazar.
Django template == operatörü etrafında boşluk gerektirir.
"""
import os

TEMPLATE_DIR = os.path.join('tickets', 'templates', 'tickets')

templates = {}

# ============= YONETIM.HTML =============
templates['yonetim.html'] = """{% extends 'tickets/base.html' %}

{% block title %}Yönetim Paneli — Şikayet Sistemi{% endblock %}

{% block content %}
<div class="panel-welcome">
    <h1>⚙️ Yönetim Paneli</h1>
    <p>Tüm şikayetleri buradan yönetebilir, durumlarını güncelleyebilirsiniz.</p>
</div>

<div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));">
    <div class="stat-card animate-in">
        <div class="stat-icon">📋</div>
        <div class="stat-number">{{ toplam }}</div>
        <div class="stat-label">Toplam</div>
    </div>
    <div class="stat-card animate-in">
        <div class="stat-icon">⏳</div>
        <div class="stat-number">{{ beklemede }}</div>
        <div class="stat-label">Beklemede</div>
    </div>
    <div class="stat-card animate-in">
        <div class="stat-icon">🔄</div>
        <div class="stat-number">{{ islemde }}</div>
        <div class="stat-label">İşlemde</div>
    </div>
    <div class="stat-card animate-in">
        <div class="stat-icon">✅</div>
        <div class="stat-number">{{ cozuldu }}</div>
        <div class="stat-label">Çözüldü</div>
    </div>
    <div class="stat-card animate-in">
        <div class="stat-icon">❌</div>
        <div class="stat-number">{{ reddedildi }}</div>
        <div class="stat-label">Reddedildi</div>
    </div>
</div>

<!-- Sekmeler -->
<div style="display: flex; gap: 0.5rem; margin-bottom: 1.5rem; flex-wrap: wrap;">
    <a href="{% url 'yonetim_paneli' %}" class="btn {% if not durum_filtre and not kategori_filtre %}btn-primary{% else %}btn-secondary{% endif %}" style="font-size:0.85rem; padding:8px 16px;">📋 Tümü</a>
    <a href="{% url 'yonetim_paneli' %}?durum=beklemede" class="btn {% if durum_filtre == 'beklemede' %}btn-primary{% else %}btn-secondary{% endif %}" style="font-size:0.85rem; padding:8px 16px;">⏳ Beklemede</a>
    <a href="{% url 'yonetim_paneli' %}?durum=islemde" class="btn {% if durum_filtre == 'islemde' %}btn-primary{% else %}btn-secondary{% endif %}" style="font-size:0.85rem; padding:8px 16px;">🔄 İşlemde</a>
    <a href="{% url 'yonetim_paneli' %}?durum=cozuldu" class="btn {% if durum_filtre == 'cozuldu' %}btn-primary{% else %}btn-secondary{% endif %}" style="font-size:0.85rem; padding:8px 16px;">✅ Çözüldü</a>
    <a href="{% url 'yonetim_paneli' %}?durum=reddedildi" class="btn {% if durum_filtre == 'reddedildi' %}btn-primary{% else %}btn-secondary{% endif %}" style="font-size:0.85rem; padding:8px 16px;">❌ Reddedildi</a>
    <a href="{% url 'yonetim_kullanicilar' %}" class="btn btn-secondary" style="font-size:0.85rem; padding:8px 16px; margin-left: auto;">👥 Öğrenciler</a>
</div>

<div class="section-title">
    <h2>📌 Şikayetler ({{ talepler|length }})</h2>
</div>

{% for talep in talepler %}
<div class="card animate-in">
    <div class="card-header">
        <h3>{{ talep.konu }}</h3>
        <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
            <span class="badge badge-{{ talep.durum }}">
                {% if talep.durum == 'beklemede' %}⏳{% elif talep.durum == 'islemde' %}🔄{% elif talep.durum == 'cozuldu' %}✅{% else %}❌{% endif %}
                {{ talep.get_durum_display }}
            </span>
            <a href="{% url 'yonetim_talep_guncelle' talep.id %}" class="btn btn-primary" style="padding: 6px 14px; font-size: 0.8rem;">✏️ Düzenle</a>
            <form method="POST" action="{% url 'yonetim_talep_sil' talep.id %}" style="margin:0;" onsubmit="return confirm('Bu şikayeti silmek istediğinize emin misiniz?');">
                {% csrf_token %}
                <button type="submit" class="btn btn-danger" style="padding: 6px 14px; font-size: 0.8rem;">🗑️ Sil</button>
            </form>
        </div>
    </div>
    <div class="card-body">
        <p>{{ talep.mesaj|truncatewords:30 }}</p>
    </div>
    <div class="card-footer">
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <span class="badge badge-kategori">📂 {{ talep.get_kategori_display }}</span>
            <span class="badge badge-oncelik-{{ talep.oncelik }}">
                {% if talep.oncelik == 'dusuk' %}🟢{% elif talep.oncelik == 'orta' %}🟡{% else %}🔴{% endif %}
                {{ talep.get_oncelik_display }}
            </span>
        </div>
        <div class="card-meta">
            <span>👤 {{ talep.ogrenci.get_full_name|default:talep.ogrenci.username }}</span>
            <span>•</span>
            <span>🎓 {{ talep.ogrenci.username }}</span>
            <span>•</span>
            <span>📅 {{ talep.tarih|date:"d M Y, H:i" }}</span>
        </div>
    </div>
    <!-- Hızlı Durum Değiştirme -->
    <div style="margin-top: 1rem; padding-top: 0.8rem; border-top: 1px solid rgba(255,255,255,0.1); display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center;">
        <span style="font-size: 0.82rem; color: var(--text-muted); margin-right: 0.3rem;">Hızlı İşlem:</span>
        {% if talep.durum != 'islemde' %}
        <form method="POST" action="{% url 'yonetim_hizli_durum' talep.id 'islemde' %}" style="margin:0;">{% csrf_token %}<button type="submit" class="btn btn-secondary" style="padding:4px 12px; font-size:0.78rem;">🔄 İşleme Al</button></form>
        {% endif %}
        {% if talep.durum != 'cozuldu' %}
        <form method="POST" action="{% url 'yonetim_hizli_durum' talep.id 'cozuldu' %}" style="margin:0;">{% csrf_token %}<button type="submit" class="btn btn-success" style="padding:4px 12px; font-size:0.78rem;">✅ Çözüldü</button></form>
        {% endif %}
        {% if talep.durum != 'reddedildi' %}
        <form method="POST" action="{% url 'yonetim_hizli_durum' talep.id 'reddedildi' %}" style="margin:0;">{% csrf_token %}<button type="submit" class="btn btn-danger" style="padding:4px 12px; font-size:0.78rem;">❌ Reddet</button></form>
        {% endif %}
    </div>
</div>
{% empty %}
<div class="empty-state">
    <div class="empty-icon">📭</div>
    <p>Bu filtrelere uygun şikayet bulunamadı.</p>
</div>
{% endfor %}
{% endblock %}
"""

# ============= YONETIM_KULLANICILAR.HTML =============
templates['yonetim_kullanicilar.html'] = """{% extends 'tickets/base.html' %}

{% block title %}Öğrenci Listesi — Yönetim{% endblock %}

{% block content %}
<div class="panel-welcome">
    <h1>👥 Kayıtlı Öğrenciler</h1>
    <p>Sisteme kayıtlı tüm öğrencilerin listesi.</p>
</div>

<div style="display: flex; gap: 0.5rem; margin-bottom: 1.5rem;">
    <a href="{% url 'yonetim_paneli' %}" class="btn btn-secondary" style="font-size:0.85rem; padding:8px 16px;">← Şikayetlere Dön</a>
</div>

<div class="section-title">
    <h2>📋 Toplam {{ ogrenciler|length }} Öğrenci</h2>
</div>

{% for profil in ogrenciler %}
<div class="card animate-in">
    <div class="card-header">
        <h3>👤 {{ profil.user.get_full_name }}</h3>
        <span class="badge badge-kategori">🎓 {{ profil.okul_no }}</span>
    </div>
    <div class="card-footer" style="border-top: none; padding-top: 0;">
        <div class="card-meta">
            <span>📋 {{ profil.user.talepler.count }} şikayet</span>
            <span>•</span>
            <span>📅 Kayıt: {{ profil.user.date_joined|date:"d M Y" }}</span>
        </div>
    </div>
</div>
{% empty %}
<div class="empty-state">
    <div class="empty-icon">👤</div>
    <p>Henüz kayıtlı öğrenci yok.</p>
</div>
{% endfor %}
{% endblock %}
"""

# Dosyaları yaz
for filename, content in templates.items():
    filepath = os.path.join(TEMPLATE_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✅ {filename} yazıldı')

print('\\nTüm template dosyaları başarıyla güncellendi!')
