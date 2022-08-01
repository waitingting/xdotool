project(xdotool)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_executable(${PROJECT_NAME})
# add_library(${PROJECT_NAME} xdotool.c)
# add_library(rpad::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
target_sources(${PROJECT_NAME}
  PRIVATE
  cmd_get_desktop_for_window.c
  cmd_getwindowname.c
  cmd_mouseup.c
  cmd_type.c
  cmd_getwindowclassname.c
  cmd_set_window.c
  cmd_set_desktop.c
  cmd_windowstate.c
  cmd_getmouselocation.c
  cmd_getwindowfocus.c
  cmd_key.c
  cmd_get_num_desktops.c
  xdotool.c
  cmd_exec.c
  cmd_windowclose.c
  cmd_mousemove.c
  cmd_windowkill.c
  cmd_getwindowgeometry.c
  xdo.c
  cmd_mousemove_relative.c
  cmd_windowunmap.c
  cmd_windowfocus.c
  cmd_set_num_desktops.c
  cmd_behave_screen_edge.c
  xdo_search.c
  cmd_window_select.c
  cmd_windowraise.c
  cmd_getwindowpid.c
  cmd_windowmove.c
  cmd_windowquit.c
  cmd_getactivewindow.c
  cmd_windowreparent.c
  cmd_sleep.c
  cmd_behave.c
  cmd_windowsize.c
  cmd_windowminimize.c
  cmd_windowactivate.c
  cmd_set_desktop_viewport.c
  cmd_search.c
  cmd_get_display_geometry.c
  cmd_windowmap.c
  cmd_mousedown.c
  cmd_click.c
  cmd_set_desktop_for_window.c
  cmd_get_desktop_viewport.c
  cmd_get_desktop.c
)

find_package(PkgConfig REQUIRED)
  pkg_check_modules(x11 REQUIRED IMPORTED_TARGET xi x11 xtst xinerama xkbcommon) 
 
target_include_directories(${PROJECT_NAME}
  PRIVATE
  ${CMAKE_SOURCE_DIR}
)

target_link_libraries(${PROJECT_NAME} -lpthread -lm -lXfixes
  PkgConfig::x11
) 