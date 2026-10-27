<section class="content-section" id="publications" aria-labelledby="publications-heading">
  <div class="section-heading"><h2 id="publications-heading">Papers &amp; notes</h2></div>
  <div class="section-body publication-list">
    {% for publication in site.data.publications.main %}
    <article class="publication">
      <div class="publication-details">
        {% if publication.conference_short %}<p class="publication-type">{{ publication.conference_short }}</p>{% endif %}
        <h3><a href="{{ publication.pdf }}">{{ publication.title }}</a></h3>
        <p class="authors">{{ publication.authors }}</p>
        {% if publication.conference %}<p class="venue">{{ publication.conference }}</p>{% endif %}
        {% if publication.notes %}<p class="venue">{{ publication.notes }}</p>{% endif %}
        <div class="publication-links">
          {% if publication.pdf %}<a href="{{ publication.pdf }}">PDF <span aria-hidden="true">↗</span></a>{% endif %}
          {% if publication.code %}<a href="{{ publication.code }}">Code <span aria-hidden="true">↗</span></a>{% endif %}
          {% if publication.page %}<a href="{{ publication.page }}">Page <span aria-hidden="true">↗</span></a>{% endif %}
          {% if publication.bibtex %}<a href="{{ publication.bibtex | relative_url }}">BibTeX <span aria-hidden="true">↗</span></a>{% endif %}
        </div>
      </div>
    </article>
    {% endfor %}
  </div>
</section>
