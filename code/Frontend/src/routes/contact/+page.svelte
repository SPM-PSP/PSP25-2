<script>
  import { Card, Dropdown, DropdownItem, Avatar, Button } from 'flowbite-svelte';
  import { DotsHorizontalOutline } from 'flowbite-svelte-icons';
</script>

<Card padding="md">
  <div class="flex justify-end">
    <DotsHorizontalOutline />
    <Dropdown class="w-36">
      <DropdownItem>Edit</DropdownItem>
      <DropdownItem>Export data</DropdownItem>
      <DropdownItem>Delete</DropdownItem>
    </Dropdown>
  </div>
  <div class="flex flex-col items-center pb-4">
    <Avatar size="lg" />
    <h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">Team</h5>
    <span class="text-sm text-gray-500 dark:text-gray-400">Designer</span>
    <div class="flex mt-4 space-x-3 rtl:space-x-reverse lg:mt-6">
      <Button>Support</Button>
      <Button color="light" class="dark:text-white">Message</Button>
    </div>
  </div>
</Card>

<Card padding="md">
  <div class="flex justify-end">
    <DotsHorizontalOutline />
    <Dropdown class="w-36">
      <DropdownItem>Edit</DropdownItem>
      <DropdownItem>Export data</DropdownItem>
      <DropdownItem>Delete</DropdownItem>
    </Dropdown>
  </div>
  <div class="flex flex-col items-center pb-4">
    <Avatar size="lg" />
    <h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">Apple</h5>
    <span class="text-sm text-gray-500 dark:text-gray-400">Developer</span>
    <div class="flex mt-4 space-x-3 rtl:space-x-reverse lg:mt-6">
      <Button>Support</Button>
      <Button color="light" class="dark:text-white">Message</Button>
    </div>
  </div>
</Card>