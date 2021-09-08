{
  description = "A very basic flake";

  outputs = { self, nixpkgs, flake-utils }:
    let
      systemDependent = flake-utils.lib.eachDefaultSystem (system:
        let pkgs = import nixpkgs { inherit system; };
        in {
          devShell = pkgs.mkShell {
            buildInputs = (with pkgs; [ pkgs.python3 ])
              ++ (with pkgs.python3.pkgs; [ django_3 flake8 black isort ]);
          };
        });
      systemIndependent = { };
    in systemDependent // systemIndependent;
}
