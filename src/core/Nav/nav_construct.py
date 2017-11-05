from .Nav import MenuItem, Nav

shared = MenuItem('Logout', 'account_logout')


member = MenuItem('Members')
member.add_sub_menu_item('Add Client', 'invite:new')

lease = MenuItem('Lease')
lease.add_sub_menu_item('New Lease', 'account_login')
lease.add_sub_menu_item('View Lease', 'invite:new')

trip = MenuItem('Trip')
trip.add_sub_menu_item('New Trip', 'trips:add')
trip.add_sub_menu_item('View Trips', 'trips:view')

wish = MenuItem('Wish')
wish.add_sub_menu_item('Add Wish', 'wish:add')
wish.add_sub_menu_item('View Wish', 'wish:list')

properties = MenuItem('Property')
properties.add_sub_menu_item('Add Property', 'property:add')



side_agent = Nav()
side_agent.add_menu(member)
side_agent.add_menu(lease)
side_agent.add_menu(trip)
side_agent.add_menu(wish)
side_agent.add_menu(properties)

top_agent = Nav()
top_agent.add_menu(shared)
top_client = Nav()
top_client.add_menu(shared)
