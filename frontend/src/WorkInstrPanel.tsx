import React from 'react';
import { Button, Stack, Text } from '@mantine/core';
import { IconExternalLink } from '@tabler/icons-react';
import { checkPluginVersion, type InvenTreePluginContext } from '@inventreedb/ui';

interface WorkInstrContext {
  url: string;
  slug: string;
}

function WorkInstrPanel({ context }: { context: InvenTreePluginContext }) {
  const { url, slug } = (context?.context as WorkInstrContext) ?? {};

  if (!url) {
    return <Text>No work instruction linked to this part.</Text>;
  }

  return (
    <Stack p="md" gap="sm">
      <Text size="sm" c="dimmed">{slug}</Text>
      <Button
        component="a"
        href={url}
        target="_blank"
        rel="noopener noreferrer"
        leftSection={<IconExternalLink size={16} />}
        variant="light"
        w="fit-content"
      >
        Open Work Instruction
      </Button>
    </Stack>
  );
}

export function renderWorkInstrPanel(context: InvenTreePluginContext) {
  checkPluginVersion(context);
  return <WorkInstrPanel context={context} />;
}
