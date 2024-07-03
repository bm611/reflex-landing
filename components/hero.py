import reflex as rx


def app_store_button(
    icon: str, text: str, color: str = "gray.100", is_highlighted: bool = False
) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.image(src=icon, width="20px", height="20px"),
            rx.text(text, class_name="text-black font-semibold"),
        ),
        class_name="border-2 rounded-full bg-gray-100 p-6",
    )


def hero() -> rx.Component:
    return rx.vstack(
        rx.heading("YOUR SUPER SMART", class_name="text-8xl", font_family="Impact"),
        rx.heading(
            "KNOWLEDGE HUB", class_name="text-8xl text-center", font_family="Impact"
        ),
        rx.heading(
            "SaveDay is a smart tool to capture, organize and utilize your knowledge",
            size="5",
        ),
        rx.button(
            rx.hstack(
                rx.image(src="/Chrome icon.svg", width="40px", height="40px"),
                rx.vstack(
                    rx.text("Install from", class_name="text-black text-xl font-bold"),
                    rx.text(
                        "Chrome Web Store",
                        class_name="text-black text-xl font-bold",
                    ),
                    spacing="0",
                ),
                class_name="flex flex-row items-center",
            ),
            class_name="mt-20 border-2 rounded-full bg-yellow-300 p-9",
        ),
        rx.hstack(
            app_store_button("/Apple icon.svg", "Apple App Store", "yellow.300", True),
            app_store_button("/Edge.svg", "Microsoft Edge Store", "yellow.300", True),
            app_store_button(
                "/Play Store icon.svg", "Google Play Store", "yellow.300", True
            ),
            class_name="mt-5",
        ),
        class_name="flex flex-col items-center pt-10 mx-auto",
    )
