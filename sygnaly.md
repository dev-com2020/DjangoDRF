# Sygnały w Django
- pre_save | post_save
- pre_delete | post_delete
- m2m_changed
- pre_migrate | post_migrate
- request_started | request_finished
- user_logged_in | user_logged_out | user_login_failed
- connection_created

### Kroki podczas pracy z sygnałem:
- definicja sygnału  (plik signals.py)
- rejestracje sygnału (@receiver)
- ładowanie sygnału (metoda ready)