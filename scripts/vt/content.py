"""Words and numbers shown on the profile panels."""

PROOF = [
    ("14", "products built, from first", "commit to production"),
    ("5+", "years as an independent", "engineer"),
    ("{total}", "contributions in the", "last 12 months"),
    ("1,000+", "test files across five", "client codebases"),
]


WORK = [
    dict(slug="thinkidx", name="ThinkIDX", link="https://www.thinkidx.com", chip="AI trust infrastructure", badge="thinkidx.com",
         light="#4B57C8", dark="#9AA4F5",
         outcome="Verified authorship and citation checks across 14 external data providers.",
         label="How it works",
         detail="Concurrent Go services, cross-encoder reranking and durable Temporal workflows.",
         stack="Go · Temporal · Next.js · PostgreSQL · Redis"),
    dict(slug="wehverse", name="WehVerse", chip="Multilingual RAG", badge="4 platforms",
         light="#8A4FB0", dark="#CDA2EA",
         outcome="Source-traceable answers across 53.8M records in 1,172 languages.",
         label="How it works",
         detail="Async embedding pipelines into pgvector. One Flutter codebase for iOS, Android, macOS and Windows.",
         stack="Python · FastAPI · Celery · pgvector · Flutter"),
    dict(slug="qnotix", name="Qnotix", chip="AI email intelligence", badge="100K+ records a day",
         light="#2F7A6E", dark="#7FCDBE",
         outcome="Turns busy inboxes into ranked work, drafted replies and Kanban tasks.",
         label="How it works",
         detail="Go and Python services answering under 200 ms, with alerts to 180+ countries.",
         stack="Go · Python · Next.js · AWS ECS · Terraform"),
    dict(slug="campusreels", name="CampusReels", chip="Multimodal moderation", badge="campusreels.com.au",
         light="#C24E39", dark="#F2977F",
         outcome="Video, image, speech and text moderation that cut manual review by over 90%.",
         label="Key decision",
         detail="The strictest of four layers wins. Only uncertain cases reach a human reviewer.",
         stack="Next.js · Google Cloud AI · MongoDB"),
    dict(slug="conde", name="Conde", link="https://apps.apple.com/us/app/conde-hair-extensions/id6762065595", chip="Mobile commerce", badge="App Store",
         light="#A35A3E", dark="#E9A88C",
         outcome="A salon pro storefront with AI shade matching and licence checks in 52 jurisdictions.",
         label="Key decision",
         detail="One binary for consumers and licensed pros, with Shopify supplying pro prices.",
         stack="Expo · React Native · FastAPI · Shopify"),
    dict(slug="cimpl3", name="CIMPL3", chip="Sustainability platform", badge="Enterprise",
         light="#3F7D4A", dark="#94D09E",
         outcome="AI-powered impact measurement and scenario building for organisations.",
         label="Key decision",
         detail="Moved booking onto Microsoft Graph with our own calendar when the embedded page was refused.",
         stack="Next.js · FastAPI · PostgreSQL · Microsoft Graph"),
    dict(slug="trellis", name="Trellis24", chip="Reporting and voice", badge="UK nurseries",
         light="#1F6A72", dark="#7FC4CB",
         outcome="Weekly reporting for a UK nursery group, with a voice planner and case management.",
         label="Key decision",
         detail="PDF dossiers render inside the Cloudflare Worker, so there is no separate service to run.",
         stack="Cloudflare Workers · Hono · Drizzle · React"),
    dict(slug="sdg", name="SDG Grants", chip="Grants discovery", badge="1,800+ grants",
         light="#2F6480", dark="#8EC2DE",
         outcome="A searchable grants database mapped to the 17 UN Sustainable Development Goals.",
         label="How it works",
         detail="AI-powered discovery, membership tiers and subscription billing.",
         stack="Next.js · FastAPI · PostgreSQL · PayPal"),
]


PRINCIPLES = [
    ("Tokens, not values", "Raw colours, ad-hoc type and untyped any are blocked on the line they are written."),
    ("Measured, not assumed", "AI features ship with eval sets in CI. Latency claims come with a load test."),
    ("Done means verified", "Tests, types, lint and guards gate every merge. Nothing ships red."),
]
CHECKS = [
    ("tokens", "no raw colours or ad-hoc type"),
    ("copy", "every string goes through copy keys"),
    ("errors", "named errors, never a generic one"),
    ("types", "no any"),
    ("env", "config read in one place"),
    ("secrets", "nothing secret in tracked files"),
    ("length", "functions and files within limits"),
    ("tests", "no skipped tests"),
    ("migrations", "no destructive renames"),
]

CONTACT = [
    ("X @victortimi_", "https://x.com/victortimi_"),
]
