---
layout: homepage
title: Teaching
permalink: /teaching/
---

<div class="teaching-text" markdown="1">
At KTH, I am a teaching assistant for [EL2700 Model Predictive Control](https://www.kth.se/student/kurser/kurs/EL2700?l=en) and supervise master's and bachelor's theses. If you are looking for a supervisor for a thesis in optimization or machine learning, you are welcome to [contact me](mailto:samuelea@kth.se).
</div>

<section class="content-section" id="supervision" aria-labelledby="supervision-heading">
  <div class="section-heading"><h2 id="supervision-heading">Supervised theses</h2></div>
  <div class="section-body">
    {% for thesis in site.data.cv.supervision %}
    <article class="cv-entry thesis-entry">
      <h3>{{ thesis.title }}</h3>
      <p>{{ thesis.author }}</p>
      <p class="entry-note">{{ thesis.degree }}, KTH · {{ thesis.year }}{% if thesis.diva %} · <a href="{{ thesis.diva }}">DiVA <span aria-hidden="true">↗</span></a>{% endif %}</p>
    </article>
    {% endfor %}
  </div>
</section>
