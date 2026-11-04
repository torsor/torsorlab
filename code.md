---
layout: page
permalink: /code/
title: code
eyebrow: the lab
lede: public repositories, by kind.
---

<p>
  <a href="https://github.com/torsor">github.com/torsor →</a> &nbsp;
  <a href="https://github.com/dkrashen">github.com/dkrashen →</a>
</p>

{% for g in site.data.repos %}
<h2>{{ g.group }}</h2>
<div class="cards">
  {%- for r in g.repos -%}
  <a class="card" href="https://github.com/{{ r.owner }}/{{ r.name }}">
    <h3 class="card__title">{{ r.name }}</h3>
    <p class="card__text">{{ r.line }}</p>
    <div class="card__foot">{{ r.owner }}/{{ r.name }} ↗</div>
  </a>
  {%- endfor -%}
</div>
{% endfor %}
