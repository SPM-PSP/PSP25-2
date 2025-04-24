<script>
  import { page } from '$app/stores';
  import { Sidebar, SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';
  import { ChartPieSolid, GridSolid, MailBoxSolid, DatabaseSolid, TerminalSolid, ArrowRightToBracketOutline } from 'flowbite-svelte-icons';
  $: activeUrl = $page.url.pathname;
</script>

<Sidebar {activeUrl}>
  <SidebarWrapper>
    <SidebarGroup>
      <SidebarItem label="Dashboard" href="/">
        <svelte:fragment slot="icon">
          <ChartPieSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
        </svelte:fragment>
      </SidebarItem>
      <SidebarItem label="Video" href="/video">
        <svelte:fragment slot="icon">
          <GridSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
        </svelte:fragment>
      </SidebarItem>
      <SidebarItem label="Alert" href="/alert">
        <svelte:fragment slot="icon">
          <MailBoxSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
        </svelte:fragment>
      </SidebarItem>
      <SidebarItem label="Data" href="/data">
        <svelte:fragment slot="icon">
          <DatabaseSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
        </svelte:fragment>
      </SidebarItem>
      <SidebarItem label="Terminal" href="/terminal">
        <svelte:fragment slot="icon">
          <TerminalSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
        </svelte:fragment>
      </SidebarItem>
      <SidebarItem label="Badge" href="/docs/components/badge">
        <svelte:fragment slot="icon">
          <ArrowRightToBracketOutline class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
        </svelte:fragment>
      </SidebarItem>
    </SidebarGroup>
  </SidebarWrapper>
</Sidebar>
