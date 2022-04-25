#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <CLI/CLI.hpp>

namespace py = pybind11;
using namespace pybind11::literals;

PYBIND11_MODULE(cli11, m) {
  py::register_exception<CLI::OptionNotFound>(m, "OptionNotFound",
                                              PyExc_KeyError);

  py::class_<CLI::App>(m, "App")
      .def(py::init<std::string, std::string>(), "app_description"_a = "",
           "app_name"_a = "")

      .def("add_flag",
           [](CLI::App &self, std::string name) { self.add_flag(name); })

      .def("__getitem__",
           py::overload_cast<std::string>(&CLI::App::count, py::const_))

      .def("parse",
           [](CLI::App& self, std::vector<std::string> vals){self.parse(vals);})

      .def("__str__", [](const CLI::App &app) { return app.help(); })

      ;
}
