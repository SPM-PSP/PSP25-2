<script>
  import { Timeline, TimelineItem } from 'flowbite-svelte';
  import { CalendarWeekSolid } from 'flowbite-svelte-icons';
</script>

<Timeline order="vertical">
  <TimelineItem title="Flowbite Application UI v2.0.0" date="Released on January 13th, 2022">
    <svelte:fragment slot="icon">
      <span class="flex absolute -start-3 justify-center items-center w-6 h-6 bg-primary-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900">
        <CalendarWeekSolid class="w-4 h-4 text-primary-600 dark:text-primary-400" />
      </span>
    </svelte:fragment>
    <p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order E-commerce & Marketing pages.</p>
  </TimelineItem>
  <TimelineItem title="Flowbite Figma v1.3.0" date="Released on December 7th, 2021">
    <svelte:fragment slot="icon">
      <span class="flex absolute -start-3 justify-center items-center w-6 h-6 bg-primary-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900">
        <CalendarWeekSolid class="w-4 h-4 text-primary-600 dark:text-primary-400" />
      </span>
    </svelte:fragment>
    <p class="text-base font-normal text-gray-500 dark:text-gray-400">All of the pages and components are first designed in Figma and we keep a parity between the two versions even as we update the project.</p>
  </TimelineItem>
  <TimelineItem title="Flowbite Library v1.2.2" date="Released on December 2nd, 2021">
    <svelte:fragment slot="icon">
      <span class="flex absolute -start-3 justify-center items-center w-6 h-6 bg-primary-200 rounded-full ring-8 ring-white dark:ring-gray-900 dark:bg-primary-900">
        <CalendarWeekSolid class="w-4 h-4 text-primary-600 dark:text-primary-400" />
      </span>
    </svelte:fragment>
    <p class="text-base font-normal text-gray-500 dark:text-gray-400">Get started with dozens of web components and interactive elements built on top of Tailwind CSS.</p>
  </TimelineItem>
</Timeline>