# django_ajax_auth

A tool for adding ajax authentication to a django site. A simple implementation using bootstrap modals and jquery for ajax.

## How it works

Use your existing auth system, simply make sure there are ID'd divs in your auth templates so they can be pulled into the modal. For example, here's a login template:

    <div class="well">
      <h1>Log In</h1>
      <form method="post">
      <div id='logindiv'>
        {% csrf_token %}
        {{ loginform.as_p }}
      </div>
      <!-- this is external because it's included in the modal -->
      <div>
        <button type="submit">Log In</button>
        <a href="/accounts/password/">Forgotten Password?</a>
      </div>
      </form>
    </div>

## Settings

    DJ_AJAX_AUTH_LOGIN_URL = "/accounts/login/"
    DJ_AJAX_AUTH_LOGIN_DIV = "logindiv"  # ID of the form div
    DJ_AJAX_AUTH_REGISTER_URL = "/accounts/signup/"
    DJ_AJAX_AUTH_REGISTER_DIV = "signupdiv"  # ID of the form div
    DJ_AJAX_AUTH_PASSWORD_URL = "/accounts/password/reset/"  # forgotten password
    DJ_AJAX_AUTH_PASSWORD_DIV = "passdiv"  # ID of the form div


    @TODO: what about using url names instead of the URL itself?
    {% url 'account_login' %}

## Assumptions

Forms submit to the same url, so /accounts/login/ would submit to /accounts/login/.