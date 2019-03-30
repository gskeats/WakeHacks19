import host


manager=host.host_manager()

host_list=manager.readhostsfromfile()
manager.print_available()