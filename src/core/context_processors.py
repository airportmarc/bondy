from invitations import forms

from .Nav.Nav import Nav, MenuItem

from .Nav.nav_construct import side_agent, top_agent, top_client

NAV_TOP_PUPLIC = {}
NAV_SIDE_PUBLIC = {}

#SHARED = [{'name': 'Logout', 'url_name': 'account_logout'}]


DEFAULT = {

}

NAV_SIDE_LABEL = 'NAV_SIDE'
NAV_TOP_LABEL = 'NAV_TOP'


def side_nav(http):
    if http.user.is_authenticated:
        if http.user.is_agent:
            return {NAV_SIDE_LABEL: side_agent.get_menu_list()}
        else:
            return "ho" # return {NAV_SIDE_LABEL: NAV_SIDE_CLIENT}
    return {NAV_SIDE_LABEL: DEFAULT}


def top_nav(http):
    if http.user.is_authenticated:
        if http.user.is_agent:
            return {NAV_TOP_LABEL: top_agent.get_menu_list()}
        else:
            return {NAV_TOP_LABEL: top_client.get_menu_list()}
    return {NAV_TOP_LABEL: DEFAULT}
